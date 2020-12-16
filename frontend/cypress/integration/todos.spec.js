describe('Tests CRUD todos', () => {
	beforeEach(() => {
		cy.visit('/')
		cy.get('.username-input').type('visitor')
		cy.get('.password-input').type('visitor')
		cy.get('.btn-connexion')
		.click()

		const nbTodos = cy.get('.todo-list li')
	})

	context('Bien vu bg', () => {
		it('Ajout todos', () => {
			cy.get('.input-value')
			.type('Test Cypress')
			.should('have.value', 'Test Cypress')
			.type('{enter}')
		})

		it('Un/Checker todos', () => {
			cy.get('.todo-list li')
			.each($el => {
				cy.wrap($el)
				.find('.checkbox')
				.click() 
			})		
		})

		it('Supprimer todos', () => {
			cy.get('.todo-list li')
			.last()
			.find('.btn-delete')
			.click()
		})
	})
})