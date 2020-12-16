describe('Tests Connexion ', () => {
	context('Bien vu bg', () => {
		it.only('Je me connecte puis deconnecte', () => {
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

			cy.get('.logout-btn')
			.click()

			cy.url().should('include', '/login')
		})
		it.only('Pas les bons identifiants', () => {
			cy.visit('/')
			cy.get('.username-input')
			.type('moi')
			.should('have.value', 'moi')

			cy.get('.password-input')
			.type('motdepasse')
			.should('have.value', 'motdepasse')
			
			cy.get('.btn-connexion')
			.click()

			cy.url().should('include', '/login')	
		})
	})
})