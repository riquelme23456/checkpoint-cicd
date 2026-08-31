# checkpoint-cicd — OpsTrack API

Repositório de checkpoint da disciplina ISW-032 (Integração e Entrega Contínua),
gerado seguindo o roteiro Repositório → Conventional Commits → Branch/PR → Conflito de merge.

## Rotas disponíveis
- `GET /` — status da API
- `GET /tickets` — lista mockada de chamados
- `GET /sobre` — nome e versão da API

## Como rodar localmente
```bash
python3 -m venv venv
source venv/bin/activate   # no Windows: venv\Scripts\activate
pip install flask
flask --app app run
```

## Relatório do conflito de merge (Bloco 4)

O conflito ocorreu no arquivo `app.py`, na linha de retorno da rota `/`. As
duas pessoas criaram branches a partir do mesmo commit na `main` e, de
propósito, alteraram a mesma linha: uma mudou a mensagem para `"operacional"`
(commit `fix: ajusta mensagem de status para operacional`) e a outra para
`"no ar"` (commit `fix: ajusta mensagem de status para no ar`). Quando a
segunda pessoa tentou mesclar seu Pull Request depois que o primeiro já havia
sido mesclado, o Git não conseguiu decidir sozinho qual das duas versões
manter e sinalizou o conflito com os marcadores `<<<<<<<`, `=======` e
`>>>>>>>`. A equipe resolveu combinando as duas versões em uma única
mensagem — `"operacional e no ar"` — editando o trecho manualmente, removendo
por completo os três marcadores antes de `git add` e `git commit`, e
concluindo o merge.
