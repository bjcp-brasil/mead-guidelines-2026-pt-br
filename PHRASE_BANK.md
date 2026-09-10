# Banco de frases repetidas

O guia original em inglês repete muitas frases padronizadas entre estilos (ex.: "Honey varieties may be declared."). Esta lista existe pra garantir que, ainda que traduzidas por pessoas diferentes, essas frases fiquem com a mesma redação em PT-BR.

Gerado por [`scripts/generate-phrase-bank.py`](scripts/generate-phrase-bank.py) a partir do texto original em inglês (commit `a1f9111`, antes de qualquer tradução). Considera frases com 2+ ocorrências idênticas (comparação exata, após normalizar espaços/aspas/travessão e remover marcação LaTeX) — variações de redação da mesma ideia não são detectadas automaticamente.

**49 frases repetidas** encontradas, cobrindo 279 ocorrências no total. **49/49** já têm uma tradução canônica sugerida — extraída de páginas já traduzidas ou, quando marcado "pré-definido", combinada antes de qualquer página ter traduzido a frase (ver [`scripts/phrase-bank-overrides.json`](scripts/phrase-bank-overrides.json)).

## Como usar

- Traduzindo ou revisando uma página: se uma frase dela aparece nesta lista **com** tradução canônica preenchida, use essa mesma redação.
- Se aparece na lista **sem** tradução canônica (coluna vazia), essa é a primeira vez que a frase está sendo traduzida — escolha a redação e, depois, rode o script de novo pra ela entrar como canônica pras próximas ocorrências.
- Depois de traduzir/revisar uma página, regenere este arquivo: `python3 scripts/generate-phrase-bank.py > PHRASE_BANK.md`.

## ✅ Nenhuma divergência encontrada

Nenhuma frase repetida com tradução conhecida está traduzida de mais de um jeito nas páginas já traduzidas — mas isso vale só pro que já foi traduzido (e só pra correspondência exata; paráfrases da mesma ideia não são pegas).

| Ocorrências | Frase original (EN) | Tradução canônica (PT-BR) | Páginas |
| --- | --- | --- | --- |
| 13x | Entrants must specify sweetness, carbonation, and strength levels. | Os participantes devem especificar os níveis de dulçor, carbonatação e força alcoólica. | M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C, M4A, M4B, M4D, M4E, M4F |
| 12x | Any bubbles, foam, head, or effervescence is based on the declared carbonation level. | Quaisquer bolhas, espuma ou efervescência são baseadas no nível de carbonatação declarado. | M1A, M1B, M1C, M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C, M4B |
| 12x | Carbonation as indicated by declared level, from still to sparkling. | A carbonatação é indicada pelo nível declarado, de tranquilo a espumante. | M1A, M1B, M1C, M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C, M4B |
| 12x | Honey varieties may be declared. | Variedades de mel podem ser declaradas. | M1A, M1B, M1C, M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C, M4C |
| 11x | Stronger meads may have a light, spicy alcohol note. | Hidroméis mais alcoólicos podem apresentar leves notas condimentadas oriundas do álcool. | M1A, M1B, M1C, M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 11x | Carbonated meads tend to express more aroma. | Hidroméis carbonatados tendem a expressar mais aromas. | M1A, M1B, M1C, M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 11x | Good to brilliant clarity. | De limpida a brilhante. | M1A, M1B, M1C, M2B, M2C, M2D, M2E, M3A, M3B, M3C, M4B |
| 11x | Greater color vibrancy and brightness is more desirable. | Cores mais vivas e brilhantes são mais desejadas. | M1A, M1B, M1C, M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 11x | Harsh, unpleasant, or excessively sulfury or yeasty fermentation characteristics are undesirable. | Características ásperas, desagradáveis ou excessivamente sulfurosas ou com notas de levedura/autólise são indesejáveis. | M1A, M1B, M1C, M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 10x | Greater clarity is more desirable. | Deseja-se uma maior limpidez. | M1A, M1B, M1C, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 10x | Balanced fermentation bouquet. | Buquê de fermentação equilibrada. | M1B, M1C, M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 10x | Tannin may make a sweeter mead seem drier. | Taninos podem fazer um hidromel suave parecer mais seco. | M1B, M1C, M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 9x | Body generally increases with sweetness and strength, typically medium-light to full. | O corpo geralmente aumenta com o dulçor e a força alcoólica, tipicamente de médio-leve a cheio. | M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C, M4B |
| 9x | Perceived alcohol by declared strength, ranging from none to noticeable and warming. | A percepção de álcool acompanha a força alcoólica declarada, variando de ausente a perceptível e com sensação de aquecimento. | M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C, M4B |
| 8x | The honey character can be subtle to strong, depending on strength and sweetness, and can express the character of flower nectar, reflective of any declared honey varietals. | O caráter de mel pode variar de sutil a intenso, dependendo da potência e dulçor e pode expressar características florais do néctar, refletindo quaisquer variedades de mel declaradas. | M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 8x | Residual sweetness and finish per the declared sweetness level. | Dulçor residual e final de acordo com o nível de dulçor declarado. | M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 8x | Acidity should be balanced, soft, or bright but not sharp. | A acidez deve ser equilibrada, macia ou vibrante, mas não agressiva. | M2A, M2B, M2C, M2D, M2E, M3A, M3B, M3C |
| 7x | A wide range of outcomes are possible depending on choices of the base mead and additional ingredients, but the final product should be balanced, pleasant, and enjoyable. | Uma ampla gama de resultados é possível, dependendo das escolhas do hidromel base e dos ingredientes adicionais, mas o produto final deve ser equilibrado, agradável e prazeroso. | M2A, M2B, M2C, M2D, M3A, M3B, M3C |
| 5x | If fruit varietals are declared, the varietal character should be noticeable. | Se variedades de fruta forem declaradas, o caráter varietal deve ser perceptível. | M2A, M2C, M2D, M2E, M3C |
| 5x | Similar to Aroma in fruit and honey character and intensity, becoming more prominent in stronger and sweeter versions. | Semelhante ao Aroma quanto a característica e intensidade de fruta e mel, se tornando mais proeminente em versões mais alcoólicas e doces. | M2A, M2B, M2C, M2D, M2E |
| 5x | The fruit character should be noticeable and balanced with the sweetness level of the mead. | O caráter da fruta deve ser perceptível e equilibrado com o nível de dulçor do hidromel. | M2A, M2B, M2C, M2D, M2E |
| 5x | Fruit must be declared. | A fruta deve obrigatoriamente ser declarada. | M2A, M2B, M2C, M2D, M2E |
| 4x | Many fruits bring natural acid and tannin that must be appropriately balanced with the base mead. | Muitas frutas conferem acidez e taninos naturais que precisam ser adequadamente equilibrados com o hidromel base. | M2A, M2C, M2D, M2E |
| 4x | The fruit character should not completely dominate the mead. | O caráter da fruta não deve dominar completamente o hidromel. | M2B, M2C, M2D, M2E |
| 4x | Some fruit may bring basic flavors (bitter, sweet, sour) in addition to their distinctive characteristics. | Algumas frutas podem conferir gostos básicos (amargo, doce, ácido) além de suas características típicas. | M2B, M2C, M2D, M2E |
| 4x | Fruited meads with other non-fruit ingredients should likely be entered as M4F Experimental Mead. | Hidroméis com frutas e outros ingredientes que não forem frutas provavelmente devem ser inscritos na categoria M4F (Experimental Mead). | M2B, M2C, M2D, M2E |
| 4x | Color as derived from the variety of fruit and honey used. | Cor proveniente da variedade de fruta e mel utilizados. | M2C, M2D, M2E, M3C |
| 3x | Color as derived from declared honey varieties, but often pale straw to gold. | A cor é proveniente das variedades de méis declarados, mas geralmente de amarelo palha a dourado. | M1A, M1B, M1C |
| 3x | Flavors similar to fermented honey aromatics in the aroma. | Sabores semelhantes aos aromas de mel fermentado em Aroma. | M1A, M1B, M1C |
| 3x | Stronger meads may have a fuller body and warmth. | Hidroméis com maior força alcoólica podem apresentar corpo mais cheio e maior aquecimento alcoólico. | M1A, M1B, M1C |
| 3x | Honey of any source. | Mel de qualquer origem. | M1A, M1B, M1C |
| 3x | Varietal honeys are expected to exhibit distinctive characteristics associated from those declared varieties. | Espera-se que os méis varietais apresentem características distintas associadas às variedades declaradas. | M1A, M1B, M1C |
| 3x | Category M1 describes the base character expected from dry, semi-sweet, and sweet meads. | A categoria M1 descreve o caráter base esperado de hidroméis secos, semi-secos e doces. | M2, M3, M4 |
| 3x | Like a M1 Traditional Mead with a noticeable fruit character. | Como um M1 Traditional Mead com um caráter frutado perceptível. | M2C, M2D, M2E |
| 3x | The fruit-derived aromatics should complement and enhance the base mead, not overwhelm it. | Os aromas provenientes da fruta devem complementar e realçar o hidromel base, não dominar. | M2C, M2D, M2E |
| 3x | Tannin from darker fruit can add some body and a drying sensation, but this should not be extreme. | Os taninos de frutas mais escuras podem conferir certo corpo e uma sensação de secura, mas isso não deve ser excessivo. | M2C, M2D, M2E |
| 3x | Spiced versions should be entered as a M3C Fruit and Spice Mead. | Versões com especiarias devem ser inscritas como M3C Fruit and Spice Mead. | M2C, M2D, M2E |
| 3x | If multiple types of fruit are declared, they do not have to be in equal proportion, bearing in mind that some fruit are stronger and more distinctive than others. | Caso sejam declarados vários tipos de frutas, elas não precisam estar em proporções iguais, leve em conta que algumas frutas são mais intensas e têm características mais marcantes do que outras. | M2D, M2E, M3C |
| 3x | Many possible descriptors exist, such as fragrant, aromatic, pungent, herbal, spicy, floral, fruity, smoky, earthy, resinous, minty, or words reminiscent of other ingredients (licorice-like, piney, citrusy, peppery). | Existem muitos descritores possíveis como perfumado, aromático, pungente, herbáceo, condimentado, floral, frutado, defumado, terroso, resinoso, mentolado ou termos que remetem a outros ingredientes (que lembram alcaçuz, pinho, frutas cítricas ou pimenta). | M3A, M3B, M3C |
| 2x | The fruit aromatics may be perceived as anything in the range from a fresh sweet juice to an aged fruit wine or Port, depending on strength and sweetness. | Os aromas frutados podem ser percebidos como algo que varia desde um suco doce fresco até um vinho de frutas envelhecido ou um vinho do Porto, dependendo da intensidade/força alcoólica e do dulçor. | M2E, M3C |
| 2x | Declared herbs and spices should be noticeable. | As ervas e especiarias declaradas devem ser perceptíveis. | M3A, M3B |
| 2x | If multiple herbs and spices are declared, they do not have to be in equal proportion, bearing in mind that some are stronger and more distinctive than others. | Caso sejam declaradas várias ervas e especiarias, elas não precisam estar em proporções iguais, leve em conta que algumas são mais intensas e têm características mais marcantes do que outras. | M3A, M3B |
| 2x | Color as derived from the variety of honey used. | A cor é proveniente da variedade de mel utilizada. | M3A, M3B |
| 2x | Spice additions may increase body, increase astringency, or add spicy-hot warming notes; none of these aspects should be excessive. | As especiarias adicionadas podem aumentar o corpo, aumentar a adstringência ou trazer notas picantes e de aquecimento; nenhum desses aspectos deve ser excessivo. | M3A, M3B |
| 2x | If spices are used in conjunction with other ingredients such as fruit, cider, or other fruit-based fermentables, then the mead should be entered as a M3C Fruit and Spice Mead. | Se as especiarias forem utilizadas em conjunto com outros ingredientes, como fruta, sidra ou outros fermentáveis à base de fruta, o hidromel deve ser inscrito como M3C Fruit and Spice Mead. | M3A, M3B |
| 2x | If spices are used in combination with other ingredients, then the mead should be entered as an M4F Experimental Mead. | Se as especiarias forem utilizadas em combinação com outros tipos de ingredientes, o hidromel deve ser inscrito como M4F Experimental Mead. | M3A, M3B |
| 2x | Perceivable herbs, spices, or spice blends must be declared. | Ervas, especiarias ou misturas de ambas perceptíveis devem ser declaradas. | M3A, M3B |
| 2x | Meads with spicy-hot flavors should specify the level of heat (mild, medium, hot) to assist judges with ordering the samples. | Hidroméis com sabores picantes de pimenta devem especificar o nível de picância (suave, médio, forte) para auxiliar os jurados na ordenação das amostras. | M3B, M3C |
| 2x | Same as the base style of mead, possibly with added tannins from the wood giving a drying quality and additional body. | A mesma do estilo-base de hidromel, possivelmente com taninos adicionais provenientes da madeira, contribuindo com maior sensação de secura e corpo. | M4D, M4E |
