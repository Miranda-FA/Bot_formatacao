from pathlib import Path
import re
from urllib.parse import quote

from src.eorbis_docbot.config import owner, repo, branch, pasta

md_path = Path("C:\\Users\\User\\Documents\\GitHub\\Bot_formatacao\\examples\\1.1.1.1 Agencias bancárias.md")
texto = md_path.read_text(encoding="utf-8")

padrao = r"!\[\[(.*?)\]\]"  

ocorrencias = re.findall(padrao, texto)

def github_raw_url(nome_arquivo: str) -> str:
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{pasta}/{quote(nome_arquivo)}"

def substituir (match):
    nome_arquivo = match.group(1)
    url = github_raw_url(nome_arquivo)
    return f" ![]({url})"

novo_texto = re.sub(padrao, substituir, texto)

saida = Path("C:\\Users\\User\\Documents\\GitHub\\Bot_formatacao\\examples\\output.md")
saida.write_text(novo_texto, encoding="utf-8")
print("Salvo em:", saida)