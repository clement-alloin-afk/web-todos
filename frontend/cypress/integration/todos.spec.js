describe('Tests CRUD todos', () => {
	beforeEach(() => {
		cy.visit('/')
		cy.get('.username-input').type('visitor')
		cy.get('.password-input').type('visitor')
		cy.get('.btn-connexion')
		.click()
	})

	context('Bien vu bg', () => {
		it('Ajout todos', () => {
			cy.get('.input-value')
			.type('Test Cypress')
			.should('have.value', 'Test Cypress')
			.type('{enter}')

			//Je regarde si le dernier des todos est 'Test Cypress'
			cy.get('.todo-list li')
			.last()
			.contains('Test Cypress')
		})	

		it('Checker/Unchecker le todo ajouté', () => {
			//Je le check
			cy.get('.todo-list li')
			.last()
			.find('.checkbox')
			.click()

			//Je regarde si le dernier des todos checker est bien 'Test Cypress'
			cy.get('.todo-list li del')
			.last()
			.contains('Test Cypress')
			.find('.checkbox')
			.click()

			// N'est plus checker , ne doit plus être le dernier des <del>
			cy.get('.todo-list li del')
			.last()
			.should('not.contain', 'Test Cypress')
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
			//Je supprime 'Test Cypress'
			cy.get('.todo-list li')
			.last()
			.find('.btn-delete')
			.click()

			//Le dernier ne devrait plus être 'Test Cypress'
			cy.get('.todo-list li')
			.last()
			.should('not.contain', 'Test Cypress')
		})
	})
})