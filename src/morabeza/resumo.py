
import csv
import sys


def ler_vendas(caminho):
    vendas = []

    with open(caminho, encoding="utf-8") as ficheiro:
        leitor = csv.DictReader(ficheiro)

        for linha in leitor:
            linha["quantidade"] = int(linha["quantidade"])
            linha["preco_unitario"] = int(linha["preco_unitario"])
            vendas.append(linha)

    return vendas


def total_venda(venda):
    return venda["quantidade"] * venda["preco_unitario"]


def faturacao_total(vendas):
    total = 0

    for venda in vendas:
        total += total_venda(venda)

    return total


def faturacao_por_ilha(vendas):
    por_ilha = {}

    for venda in vendas:
        ilha = venda["ilha"]
        valor = total_venda(venda)

        por_ilha[ilha] = por_ilha.get(ilha, 0) + valor

    return por_ilha


def ilha_top(por_ilha):
    return max(por_ilha, key=por_ilha.get)


def main():
    caminho = sys.argv[1] if len(sys.argv) > 1 else "data/vendas_amostra.csv"

    vendas = ler_vendas(caminho)
    total = faturacao_total(vendas)
    por_ilha = faturacao_por_ilha(vendas)
    melhor_ilha = ilha_top(por_ilha)

    print(f"Total de vendas: {len(vendas)}")
    print(f"Faturação total: {total} CVE")
    print("\nFaturação por ilha:")

    for ilha, valor in sorted(por_ilha.items()):
        print(f"{ilha}: {valor} CVE")

    print(f"\nIlha com maior faturação: {melhor_ilha}")

def faturacao_mensal(vendas):
    por_mes = {}

    for venda in vendas:
        mes = venda["data"][:7]
        valor = total_venda(venda)
        por_mes[mes] = por_mes.get(mes, 0) + valor

    return por_mes

def formatar_cve(valor):
    return f"{valor:,.0f}".replace(",", " ").replace(".", ",") + " CVE"

if __name__ == "__main__":
    main()
