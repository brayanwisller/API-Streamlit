# 📊 Streamlit Interactive Dashboard

Este é um Web App de dashboard interativo desenvolvido com **Streamlit**, focado em oferecer uma interface personalizada com navegação moderna, gerenciamento de estados e visualização de dados dinâmica.

## 🚀 Funcionalidades Principais

* **Navegação:** Barra lateral (sidebar) com efeito *hover* utilizando a biblioteca `st_on_hover_tabs`.
* **Modo Escuro Dinâmico:** Alternância de tema (Dark/Light) que sincroniza cores de fundo, textos e componentes via CSS injetado.
* **Validação Inteligente:** Sistema de login com validação de Regex para telefones brasileiros e restrição de domínio para e-mails (Gmail).
* **Visualização de Dados:** Gerenciamento de gráficos de linha, barras e área com suporte a `session_state`.
* **Exportação de Dados:** Cache de dados para download de tabelas em formato CSV.
* **Feedback Interativo:** Sistema de avaliação por estrelas com lógica de resposta condicional.

## 🛠️ Tecnologias e Bibliotecas

* **Python** (Core do projeto)
* **Streamlit** (Interface Web)
* **Pandas & Numpy** (Manipulação de dados)
* **st-on-hover-tabs** (Sidebar personalizada)
* **streamlit-autorefresh** (Atualização dinâmica da UI)
* **CSS3** (Customização de componentes e ocultação de menus padrão)

## 📁 Estrutura de Arquivos

* `test.py`: O código principal da aplicação.
* `style.css`: Arquivo contendo as definições de estilo para a sidebar e elementos globais.
* `requirements.txt`: Lista de dependências para instalação.

## ⚙️ Instalação e Execução

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/brayanwisller/api-streamlit.git](https://github.com/brayanwisller/api-streamlit.git)
   cd api-streamlit
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
3. **Execute o app:**
   ```bash
   streamlit run test.py

## 🎨 Customização de Interface

O projeto remove os elementos padrão do Streamlit (como o menu superior e a linha de decoração) através de injeção de CSS para garantir uma aparência de "Software Independente". A lógica de cores é controlada dinamicamente:

  - Light Mode: Tons azulados e fundos claros.

  - Dark Mode: Tons pretos e cinzas profundos para conforto visual.

---

Desenvolvido como projeto para fins de teste e aprendizado de ferramentas de interface.
