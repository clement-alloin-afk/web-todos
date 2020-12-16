describe('SMoke tests', () => {
	/*beforeEach(() => {
		cy.request('GET', '/api/todos')
		.its('body')
		.each(todo => cy.request('DELETE', '/api/todo/${todo.uuid}'))
	})*/

	context('Connexion', () => {
		it.only('Je me connecte bg', () => {
			cy.visit('/')
			cy.get('.username-input')
			.type('visitor')
			.should('have.value', 'visitor')

			cy.get('.password-input')
			.type('visitor')
			.should('have.value', 'visitor')
			
			cy.get('.btn-connexion')
			.click()

			cy.url().should('not.include', '/login')
			
		})
	})
})