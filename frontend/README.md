# TuneScore Frontend

Bem-vindo ao **TuneScore**, uma plataforma para avaliar músicas, como um Letterboxd para música! Este é o frontend do projeto, construído com **React** e **Vite**, que roda a interface do usuário.

## Pré-requisitos

Para rodar o projeto, você precisa do **Node.js** instalado:
- Baixe a versão recomendada em [nodejs.org](https://nodejs.org).
- Verifique se está instalado abrindo o terminal (Prompt de Comando, PowerShell ou Terminal no macOS/Linux) e rodando:
  ```
  node -v
  npm -v
  ```
  Você deve ver versões como `v20.17.0` (Node) e `10.8.1` (npm).

## Como rodar o projeto

1. **Entre na pasta do frontend**:
   No terminal, navegue até a pasta do projeto:
   ```
   cd caminho/para/tunescore/frontend
   ```
   Exemplo: `cd C:\Users\SeuNome\Documents\Estudos\Linguagens\Python\TuneScore\frontend`

2. **Instale as dependências**:
   Rode o comando abaixo para instalar o React, Vite e outras bibliotecas:
   ```
   npm install
   ```

3. **Inicie o servidor**:
   Rode o comando para abrir o site:
   ```
   npm run dev
   ```
   - Isso abrirá o TuneScore em `http://localhost:5173` (ou outra porta, se ocupada).
   - Abra o link no navegador (Chrome, Firefox, etc.) para ver a interface.

4. **Parar o servidor**:
   Para parar o site, pressione `Ctrl + C` no terminal e confirme com `Y` (ou `S`).

## Solução de problemas

- **Erro no PowerShell (Windows)**: Se aparecer "execução de scripts foi desabilitada", abra o PowerShell como administrador (pesquise no menu Iniciar, clique com o botão direito e selecione "Executar como administrador") e rode:
  ```
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```
  Confirme com `Y` (ou `S`) e tente novamente.

- **Erro "npm não encontrado"**: Reinstale o Node.js em [nodejs.org](https://nodejs.org).

- **Porta ocupada**: Se `localhost:5173` não abrir, pare o servidor com `Ctrl + C` e rode `npm run dev` novamente. Ou mude a porta em `vite.config.js`:
  ```javascript
  export default {
    server: {
      port: 3000,
    },
  }
  ```

## Estrutura do projeto

- `src/App.jsx`: Onde você edita a interface principal do TuneScore (ex.: listas de músicas, formulários de avaliação).
- `src/index.css`: Para estilos visuais.
- `public/`: Para arquivos como imagens ou ícones.

## Sobre o projeto

O frontend usa **React** para criar a interface e **Vite** para rodar o servidor rápido com Hot Module Replacement (HMR), que atualiza a página automaticamente ao editar o código. Ele inclui regras básicas de ESLint para manter o código organizado.

Se quiser adicionar mais recursos (ex.: suporte a TypeScript), veja o [template TypeScript do Vite](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts).

## Próximos passos

- Edite `src/App.jsx` para criar a interface do TuneScore, como uma lista de músicas ou um formulário para avaliações.
- Conecte com o backend (na pasta `../backend`, em Python) para salvar e buscar dados.
- Para aprender mais, veja a documentação do [React](https://react.dev) e [Vite](https://vitejs.dev).

Se precisar de ajuda, pergunte ao Ygor ou aos amigos desenvolvedores!