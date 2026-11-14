describe('Sistema de Gestão de Estoque', () => {
  it('Deve carregar a página inicial corretamente', () => {
    cy.visit('http://127.0.0.1:5000');
    cy.get('h1').should('contain', 'Controle de Estoque');
  });
});