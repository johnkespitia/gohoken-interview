/// <reference types="cypress" />
describe('Home Page', () => {
    it('renders images correctly', () => {
        cy.visit('/');
        cy.get('h1').should('contain', 'Random Images!');
        cy.get('.image-grid')
            .find('img')
            .should('have.length.gt', 3);
    });
});
