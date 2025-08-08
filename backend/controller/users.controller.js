const db = require('../db')
class UsersController {
    async createUser(req, res) {
        try {
        const {tg_id, name, surname, score, maths, rus, inf} = req.body
        const newUser = await db.query(`INSERT INTO users (tg_id, name, surname, score, maths, rus, inf) values ($1, $2, $3, $4, $5, $6, $7) RETURNING *`, [tg_id, name, surname, score, maths, rus, inf])
        res.json(newUser.rows[0])
        }
        catch (e) {
            res.status(500).json({"message": e})
        }
    }
    async getUsers(req, res) {
        const users = await db.query(`SELECT * FROM users`)
        res.json(users.rows)
    }
    async getOneUser(req, res) {
        const id = req.params.id
        const item = await db.query(`SELECT * FROM users WHERE id = $1`, [id])
        res.json(item.rows[0])
    }
    async updateUser(req, res) {
        const {id, tg_id, name, surname, score, maths, rus, inf} = req.body
        const user = await db.query(`UPDATE users set tg_id = $1, name = $2, surname = $3, score = $8, maths = $4, rus = $5, inf = $6 WHERE id = $7 RETURNING *`, [tg_id, name, surname, maths, rus, inf, id, score])
        res.json(user.rows[0])
    }
    async deleteUser(req, res) {
        const id = req.params.id
        const user = await db.query(`DELETE FROM users WHERE id = $1`, [id])
        res.json(user.rows[0])
    }
    async findUser(req, res){
        const tg_id = req.params.id
        const user = await db.query(`SELECT * FROM users WHERE tg_id = $1`, [tg_id])
        res.json(user.rows[0])
    }
}

module.exports = new UsersController()