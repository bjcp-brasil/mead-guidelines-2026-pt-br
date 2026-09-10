# mead-guidelines-2026-pt-br

Tradução PT-BR do BJCP Mead Style Guidelines 2026, em LaTeX. Estruturado seguindo o
padrão do projeto irmão [`bjcp-brasil/cider-guidelines-2025-pt-br`](https://github.com/bjcp-brasil/cider-guidelines-2025-pt-br)
(mesmo dono, mesma convenção de arquivos/CI/site).

Fonte original em inglês: `2026_Guidelines_Mead-final.pdf` (na raiz, **nunca
commitado** — mesma convenção do cider, que também não versiona o PDF fonte).
O `.tex` é a única fonte da verdade depois de estruturado.

## Estrutura do repo

- `main.tex`, `frontpage.tex` — shell do documento e capa
- `introduction-to-the-2026-mead-guidelines/`, `introduction-to-mead-styles/` — introdução/preâmbulo
- `m1-traditional-mead/` … `m4-specialty-mead/` — categorias de estilo, cada uma com `header.tex` (preâmbulo da categoria) + um `.tex` por estilo (ex.: `m1-a-dry-mead.tex`)
- `TRANSLATION_STATUS.md` — status de tradução/revisão por página, com % ponderada por caractere
- `PHRASE_BANK.md` — banco de frases repetidas entre estilos, pra manter tradução consistente entre páginas/tradutores (ver seção própria abaixo)
- `scripts/generate-phrase-bank.py` — gera o `PHRASE_BANK.md`
- `website/` — mirror HTML (Docusaurus), publicado via GitHub Pages. `website/docs/` é gerado no CI, nunca commitado.
- `.github/workflows/` — `build-check.yml` (valida build em qualquer branch) e `deploy-pages.yml` (publica em `main`)

Todo o texto começou em inglês (extraído do PDF) e vai sendo traduzido página por
página, mantendo os comandos LaTeX e os `\textbf{Label}:` de cada campo (Impressão
Geral, Aroma, Aparência, Sabor, Sensação na Boca, Ingredientes, Comentários,
Instruções para Inscrição, Exemplos Comerciais).

## Antes de qualquer commit envolvendo `.tex`

1. **Compilar e checar erro de verdade**, não só "não travou":
   ```
   latexmk -pdf -g -synctex=1 -interaction=nonstopmode main.tex
   grep -n "^!" main.log   # deve vir vazio
   pdfinfo main.pdf | grep Pages   # deve ser 17
   ```
   `-g` força rebuild completo (senão o latexmk pula achando que já está atualizado)
   e `-synctex=1` é necessário explicitamente — o ambiente não gera `.synctex.gz` por
   padrão sem essa flag.

2. **Checar os bugs recorrentes** que já apareceram nas traduções (grep antes de
   confiar no compile limpo, já que nem todo erro de conteúdo quebra o LaTeX):
   - `\it{palavra}` — **não** limita itálico à palavra (é uma declaração de fonte,
     não uma macro com argumento). Usar sempre `\textit{palavra}`.
   - `&` sem escape fora de tabela — vira "Misplaced alignment tab character" e
     quebra a compilação. Precisa ser `\&`.
   - `\url{URL}{TEXTO}` — `\url` só aceita 1 argumento. Link com texto customizado
     é `\href{URL}{TEXTO}`.
   - `\textbf{Label}:texto` sem espaço depois dos dois-pontos — sai grudado no PDF
     ("Boca:A mesma"). Sempre `\textbf{Label}: texto`.
   - Parágrafo duplicado — o original em inglês não removido, tradução adicionada
     do lado. Sobra o mesmo conteúdo duas vezes no PDF.
   - Asterisco de markdown sobrando dentro de `\textit{...}` (`\textit{*texto*}`) —
     vira caractere `*` literal impresso.
   - Tabelas LaTeX: usar `booktabs` (`\toprule`/`\midrule`/`\bottomrule`), não
     `tabular` puro — o pandoc (usado no site) só detecta header de tabela assim.
     Conferir contagem de colunas do `{lcccc}` bate com as células de cada linha.

   Comandos rápidos:
   ```
   grep -rn '\\it{' <arquivo>
   grep -nP '(?<!\\)&' <arquivo>
   grep -n '}:[A-Za-z]' <arquivo>
   ```

3. Se achar algo que parece errado mas não é claramente um bug de sintaxe (ex.:
   texto duplicado, frase com redação diferente do que já existe em outra página) —
   **avisar e perguntar antes de mexer**, não corrigir silenciosamente. Bug de
   sintaxe que quebra compilação (item 2) pode corrigir direto, só avisando depois.

## `TRANSLATION_STATUS.md`

Tabela com uma linha por página (arquivo `.tex` de conteúdo — não `index.tex`),
colunas Tradução/Revisão (✅ Traduzido / ⬜ Pendente), na ordem em que aparecem no
guia (mesma ordem dos `\input` do `main.tex`).

No topo, duas porcentagens **ponderadas por caractere** (não por número de
páginas — uma entrada curta e uma longa não pesam igual):

```python
# pra cada página: wc -m do arquivo inteiro
# Tradução % = soma de chars das páginas ✅ / soma de chars de todas
# Revisão % = idem, mas pra coluna Revisão
```

Sempre que uma página muda de status (traduzida ou revisada), atualizar a linha
dela **e** recalcular as duas porcentagens no topo — nunca deixar desatualizado.

**A coluna Revisão só marca ✅ com revisão humana.** Uma passada de revisão
feita pelo Claude (gramática, concordância, bugs de LaTeX, convergência do
phrase bank etc.) não conta como Revisão para este fim — mesmo corrigindo
erros reais, não marque a página como revisada nessa coluna. Só o usuário
(ou outra pessoa humana) revisando marca essa coluna.

## `PHRASE_BANK.md`

O guia em inglês repete muita frase padronizada entre estilos (~40% de todo o
conteúdo). Esse arquivo lista essas frases repetidas e, pra cada uma, a tradução
canônica em PT-BR já usada (quando já existe alguma página traduzida com ela).

- **Nunca editar `PHRASE_BANK.md` na mão para mudar a tradução canônica de uma
  frase.** Ele é gerado a partir dos `.tex` reais; editar só o `.md` cria uma
  divergência que desaparece (silenciosamente errada) na próxima regeneração.
  Pra mudar a redação canônica de uma frase: editar a página `.tex` que a contém,
  depois regenerar o bank.
- Regenerar depois de qualquer tradução/revisão:
  ```
  python3 scripts/generate-phrase-bank.py > PHRASE_BANK.md
  ```
- O script compara com o texto original em inglês do commit `a1f9111` (primeira
  versão, 100% em inglês, antes de qualquer tradução) — é a baseline pra saber
  quais frases se repetem. Não mudar essa constante a menos que esse commit seja
  perdido/reescrito.
- O script também detecta **divergência**: mesma frase EN traduzida de jeitos
  diferentes em páginas diferentes (guias com `⚠️` na tabela + seção de resumo).
  Se aparecer divergência ao regenerar, resolver escolhendo uma redação e
  propagando pra todas as páginas envolvidas antes de commitar — é exatamente o
  cenário que esse arquivo existe pra pegar.
- Antes de traduzir uma página nova, vale checar o bank primeiro — se uma frase
  dela já tem tradução canônica, usar a mesma; se não tem, essa tradução vira a
  canônica pras próximas ocorrências.
- Limitação conhecida: é matching exato (após normalizar espaço/aspas/travessão),
  não pega paráfrase da mesma ideia com redação diferente.
- `header.tex` de categoria (M2/M3/M4, o preâmbulo de cada categoria) não usa
  `\textbf{Label}:` — é só um ou mais parágrafos `\textit{...}` soltos. O script
  trata isso com um extrator separado (`extract_textit_blocks`/`get_blocks`),
  já que esses arquivos não têm nenhum campo rotulado pra alinhar por label.
- **Quando uma página nova/PR chega com redação diferente da canônica já
  estabelecida (nos overrides ou em outra página real), o canônico já
  decidido é que manda — corrija a página nova pra bater com ele, não trate
  como uma opção equivalente pra perguntar ao usuário de novo.** Só pergunte
  se o próprio usuário disser que quer mudar o canônico.
- **Escopo estrito**: ao corrigir uma divergência ou aplicar o canônico,
  mexer *só* na frase exata listada no bank/override — nunca aproveitar pra
  fazer uma varredura mais ampla de termo (ex.: trocar toda ocorrência de
  "teor alcoólico" por "força alcoólica" no resto do texto da página só
  porque apareceu numa frase do bank). Se notar um padrão de terminologia
  mais amplo que poderia valer a pena, mencionar pro usuário, mas não agir
  sem pedido explícito.

### `scripts/phrase-bank-overrides.json` — traduções pré-definidas

Às vezes uma tradução de uma frase repetida é decidida **antes** de qualquer
página com essa frase ter sido traduzida (ex.: alguém manda um lote de frases
já traduzidas como referência pra quem for traduzir M2/M3 depois). Isso entra
nesse arquivo (`{"frase em inglês": "tradução em PT-BR"}`), nunca direto no
`PHRASE_BANK.md` — mesma razão do item acima: só esse `.json` sobrevive a uma
regeneração.

- Antes de adicionar uma entrada nova, **sempre checar se já existe uma
  tradução real vinda de alguma página já traduzida** (rodar o bank sem a
  entrada nova e comparar) — se houver conflito, perguntar ao usuário qual
  prevalece em vez de assumir. Já aconteceu de uma frase parecer "sem
  tradução ainda" só porque o script tinha um bug de detecção (ver bug do
  `header.tex` acima) e na real já estava traduzida numa página real.
  Página real sempre tem prioridade por padrão, a menos que o usuário decida
  o contrário explicitamente.
- Uma vez que uma página real traduz essa frase de um jeito diferente do que
  está no override, isso aparece como divergência normal (override conta
  como mais uma "fonte", rotulada "pré-definido" na saída) — resolve-se do
  mesmo jeito que qualquer outra divergência.

## Créditos de tradução

Quando o usuário disser que a tradução de uma página foi feita por outra pessoa
(ex.: "isso foi traduzido pelo Maycon"):

- **Não** trocar o autor do commit git — manter o autor padrão da sessão (usuário
  logado no `gh`/`git`), a menos que instruído explicitamente o contrário.
- Adicionar uma linha `Translation-by: Nome da Pessoa` no corpo da mensagem de
  commit.
- Conferir/atualizar a tabela de créditos em `frontpage.tex` (linha "2026
  Tradução para Português Brasileiro:") pra incluir o nome, se ainda não estiver
  lá.

## Git / commits

- **Nunca** dar `git add -A` puro — sempre excluir o PDF fonte:
  `git add -A -- ':!2026_Guidelines_Mead-final.pdf'`. Ele não deve ser versionado
  (mesma convenção do cider-guidelines).
- Fluxo padrão estabelecido nesta sessão: compilar → checar erro → conferir bugs
  recorrentes → atualizar `TRANSLATION_STATUS.md` (status + %) → regenerar
  `PHRASE_BANK.md` se alguma página com frase repetida mudou → `git add` (exceto
  PDF) → commit com mensagem descrevendo o que mudou → **push** (o padrão até
  agora sempre incluiu push depois do commit, mesmo quando só "faça um commit"
  foi pedido).
- Mensagens de commit em inglês (consistente com o restante do histórico), corpo
  explicando o quê e por quê quando não for óbvio.
- Repo: `bjcp-brasil/mead-guidelines-2026-pt-br` (GitHub). Pages habilitado via
  `build_type: workflow`, publica em
  https://bjcp-brasil.github.io/mead-guidelines-2026-pt-br/.

## Compilação local

Requer TeX Live (`latexmk`, `pdflatex`) e, pro site, Node 20+ e Docker (o
`website/scripts/generate-docs.mjs` usa `pandoc/core:2.9` via Docker pra
converter `.tex` → Markdown). Ver `website/README.md` para o pipeline completo
do site.
