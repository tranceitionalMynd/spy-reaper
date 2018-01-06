conn = new Mongo();
db = conn.getDB('sample');
db = db.getSiblingDB('algorithmHistory');

db.transactions.find().forEach( function(thisDoc) {
    db.transactions.remove({ "_id" : thisDoc._id });
}); 

db.transactions.insert({'ticker' : 'SPY', 'date': '2017-01-01', 'type': 'buy', 'shares': 10, 'price': 10.1 });
db.transactions.insert({'ticker' : 'SPY', 'date': '2017-01-02', 'type': 'sell', 'shares': 10, 'price': 11.1 });
db.transactions.insert({'ticker' : 'SPY', 'date': '2017-01-03', 'type': 'buy', 'shares': 10, 'price': 11.2 });
db.transactions.insert({'ticker' : 'SPY', 'date': '2017-01-04', 'type': 'sell', 'shares': 10, 'price': 10.5 });
db.transactions.insert({'ticker' : 'SPY', 'date': '2017-01-05', 'type': 'buy', 'shares': 10, 'price': 10.7 });
db.transactions.insert({'ticker' : 'SPY', 'date': '2017-01-06', 'type': 'sell', 'shares': 10, 'price': 15.5 });

allTransactions = db.transactions.find()

while (allTransactions.hasNext()) {
  printjson(allTransactions.next());
}
