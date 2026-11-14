# sistema-estoque

O sistema de controle de estoque foi concluído com sucesso, integrando um frontend minimalista (HTML/JS), backend em Python (Flask) e banco de dados relacional MySQL com restrições de integridade.

Para assegurar a qualidade e o funcionamento da aplicação, foi implementada uma pipeline de integração contínua (CI) via GitHub Actions, que provisiona automaticamente o banco de dados MySQL em container, inicializa o servidor Flask e executa testes automatizados de caixa-preta (E2E) com Cypress em modo headless a cada atualização no repositório. Todo o fluxo de build, persistência de dados e validação da interface foi executado e aprovado com sucesso na nuvem em pouco mais de 1 minuto.

<img width="1877" height="896" alt="image" src="https://github.com/user-attachments/assets/f7a39a5e-26f9-4e8b-835c-b69e3f71827b" />

