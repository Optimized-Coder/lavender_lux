from ..extensions import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    ingredients = db.Column(db.Text, nullable=False)
    garnish = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Recipe: {self.title}>'

    @property
    def generate_ingredients(self):
        return self.ingredients.split('\n')
    
    @property
    def generate_instructions(self):
        return self.ingredients.split('\n')