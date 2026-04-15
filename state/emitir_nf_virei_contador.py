#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
from datetime import date
from pathlib import Path

import requests

BASE_URL = "https://cliente.vireicontador.com.br"
DEFAULT_OUTPUT_DIR = Path("/home/marcelo/.openclaw/workspace/state/nf-teste")


def env_or_arg(value, env_name):
    return value or os.environ.get(env_name)


def login(session, login_value, password):
    resp = session.post(
        f"{BASE_URL}/api/auth",
        json={"login": login_value, "password": password},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["token"]


def auth_headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def get_service(session, token, service_id):
    resp = session.get(f"{BASE_URL}/api/servicos/{service_id}", headers=auth_headers(token), timeout=30)
    resp.raise_for_status()
    return resp.json()


def build_payload(args, service):
    amount = round(float(args.amount), 2)
    item_total = round(amount * float(args.quantity), 2)
    return {
        "id": 0,
        "type": "AVULSA",
        "number": args.number,
        "clientId": args.client_id,
        "saleDate": args.sale_date,
        "startDate": args.sale_date,
        "firstSaleDate": args.sale_date,
        "generateDay": None,
        "freqValue": 1,
        "freqUnit": "MES",
        "endAt": None,
        "discountType": "R$",
        "discountValue": 0,
        "totalGeneral": item_total,
        "status": "PENDENTE",
        "items": [
            {
                "productId": args.service_id,
                "description": args.description,
                "quantity": float(args.quantity),
                "unitPrice": amount,
                "total": item_total,
            }
        ],
        "cnaeCodigo": service.get("cnaeCodigo") or "",
        "itemLc116": service.get("itemLc116") or "",
        "nbsCodigo": service.get("nbsCodigo") or "",
        "codigoServicoMunicipio": service.get("codigoServicoMunicipio") or "",
        "municipioPrestacaoId": service.get("municipioPrestacaoId") or 0,
        "municipioPrestacaoNome": service.get("municipioPrestacaoNome") or "",
        "municipioPrestacaoUf": service.get("municipioPrestacaoUf") or "",
        "tipoTributacao": service.get("tipoTributacao") or "",
        "issAliquota": service.get("issAliquota") or 0,
        "pisAliquota": service.get("pisAliquota") or 0,
        "cofinsAliquota": service.get("cofinsAliquota") or 0,
        "csllAliquota": service.get("csllAliquota") or 0,
        "inssAliquota": service.get("inssAliquota") or 0,
        "irAliquota": service.get("irAliquota") or 0,
        "reterIss": bool(service.get("reterIss")),
        "reterPis": bool(service.get("reterPis")),
        "reterCofins": bool(service.get("reterCofins")),
        "reterCsll": bool(service.get("reterCsll")),
        "reterInss": bool(service.get("reterInss")),
        "reterIr": bool(service.get("reterIr")),
    }


def create_sale(session, token, payload):
    resp = session.post(f"{BASE_URL}/api/sales", headers=auth_headers(token), json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()


def emit_sale(session, token, sale_id):
    resp = session.post(f"{BASE_URL}/api/sales/{sale_id}/emitir-nfse", headers=auth_headers(token), json={}, timeout=60)
    resp.raise_for_status()
    return resp.json()


def sync_sale(session, token, sale_id):
    resp = session.post(f"{BASE_URL}/api/sales/{sale_id}/sync-nfse", headers=auth_headers(token), json={}, timeout=60)
    resp.raise_for_status()
    return resp.json()


def download_pdf(session, token, sale_id, output_path):
    resp = session.get(f"{BASE_URL}/api/sales/{sale_id}/nfse/pdf", headers={"Authorization": f"Bearer {token}"}, timeout=60)
    resp.raise_for_status()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(resp.content)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Emissão assistida de NFSe via API da Virei Contador")
    parser.add_argument("--login")
    parser.add_argument("--password")
    parser.add_argument("--client-id", type=int, required=True, help="ID do tomador/cliente no portal")
    parser.add_argument("--service-id", type=int, required=True, help="ID do serviço cadastrado da Leevre no portal")
    parser.add_argument("--number", type=int, required=True, help="Próximo número sugerido pelo emissor")
    parser.add_argument("--amount", type=float, required=True, help="Valor unitário da nota")
    parser.add_argument("--description", required=True, help="Descrição do serviço")
    parser.add_argument("--sale-date", default=str(date.today()), help="Data da nota, YYYY-MM-DD")
    parser.add_argument("--quantity", type=float, default=1)
    parser.add_argument("--emit", action="store_true", help="Além de criar a venda, emitir a NFSe")
    parser.add_argument("--sync-attempts", type=int, default=5)
    parser.add_argument("--sync-wait-seconds", type=int, default=2)
    parser.add_argument("--download-pdf", action="store_true")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    args = parser.parse_args()

    login_value = env_or_arg(args.login, "VIREI_LOGIN")
    password = env_or_arg(args.password, "VIREI_PASSWORD")
    if not login_value or not password:
        print("Erro: informe --login/--password ou defina VIREI_LOGIN e VIREI_PASSWORD.", file=sys.stderr)
        return 2

    session = requests.Session()
    token = login(session, login_value, password)
    service = get_service(session, token, args.service_id)
    payload = build_payload(args, service)
    created = create_sale(session, token, payload)

    result = {
        "created": created,
        "emitted": None,
        "sync": [],
        "pdf": None,
    }

    if args.emit:
        emitted = emit_sale(session, token, created["id"])
        result["emitted"] = emitted
        current = emitted
        for _ in range(max(args.sync_attempts, 0)):
            time.sleep(max(args.sync_wait_seconds, 0))
            current = sync_sale(session, token, created["id"])
            result["sync"].append(current)
            if current.get("nfsStatus") in {"EMITIDA", "ERRO", "CANCELADA"}:
                break

        if args.download_pdf and current.get("nfsStatus") == "EMITIDA":
            safe_name = created.get("clientName", f"sale-{created['id']}").replace("/", "-")
            output_path = Path(args.output_dir) / f"NFSE-{safe_name}-{current.get('number', created['id'])}.pdf"
            saved = download_pdf(session, token, created["id"], output_path)
            result["pdf"] = str(saved)

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
