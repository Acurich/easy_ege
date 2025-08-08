const Pool = require('pg').Pool
const pool = new Pool({
    user: 'c65504_ege_scrapper_bot_na4u_ru',
    password: 'SuJzaSircubop14',
    host: 'postgres.c65504.h2',
    port: '5432',
    database: 'c65504_ege_scrapper_bot_na4u_ru'
})


module.exports = pool