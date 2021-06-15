import mongoose from 'mongoose';
import {database as databaseConfig} from "./config/database";

export class Database {
    async connect() {
        await mongoose.connect(`mongodb://${databaseConfig.host}:${databaseConfig.port}/${databaseConfig.name}`, {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
    }

    close() {
        mongoose.connection.close();
    }
}
