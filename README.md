## Projeto: Decodificar Notas em Base64

Este projeto contém um script em Python que lê um arquivo JSON contendo notas fiscais codificadas em Base64, decodifica cada XML, extrai o valor da tag `<nNF>` e salva cada nota no formato XML em uma pasta de saída.

---

### Estrutura do projeto

```bash
├── data/
│   └── notas.json      # JSON de entrada com as notas codificadas
├── decodificar_notas.py # Script principal
└── out/                # Saída com os arquivos XML decodificados
```

---

### Mockup de `data/notas.json`

```json
{
  "xmls": [
    "BASE64_XML_1",
    "BASE64_XML_2",
    "BASE64_XML_3"
  ]
}
```
---

### Pré-requisitos

* Ter python instalado (versão utilizada no projeto: 3.10)

---

### Como usar

1. **Clone o repositório** ou copie os arquivos para uma pasta local.
2. **Adicione dados ao arquivo notas.json** na pasta `data/`. Conforme o mockup acima.
3. **Execute o script**:

   ```bash
   python decodificar_notas.py
   ```
4. **Verifique a saída**: os arquivos XML serão gerados na pasta `out/`, com nomes no formato `NFe<nNF>.xml`.


