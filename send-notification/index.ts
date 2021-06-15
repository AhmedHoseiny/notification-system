import { Consumer } from "./handlers/consumer";
import {Database} from "./database";

const db = new Database();
db.connect();

const consumerHandler = new Consumer();

consumerHandler.connect();

// If the Node process ends, close the Mongoose connection
process.on('SIGINT', function() {
  db.close()
});

process.on('SIGTERM',function() {
  db.close()
});

