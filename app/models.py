


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key = True)
    family_name = db.Column(db.String(50), nullable = True)
    address = db.Column(db.String(50), nullable = False)
    payments = db.relationship('Payment', backref='role')
    
    def __repr__(self):
        return '<Customer %r>' % self.address 
    
class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable = False)
    address_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable = False)
    
    def __repr__(self):
        return '<Payment %r>' % self.date