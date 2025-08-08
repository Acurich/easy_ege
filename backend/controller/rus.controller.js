const db = require('../db')
class RusController {
    async createRus(req, res) {
        try {
        const {task_id, task_type, task, task_img, answer, answer_img} = req.body
        const newRus = await db.query(`INSERT INTO rus (task_id, task_type, task, task_img, answer, answer_img) values ($1, $2, $3, $4, $5, $6) RETURNING *`, [task_id, task_type, task, task_img, answer, answer_img])
        res.json(newRus.rows[0])
        }
        catch (e) {
            res.status(500).json({"message": e})
        }
    }
    async getRus(req, res) {
        const rus = await db.query(`SELECT * FROM rus`)
        res.json(rus.rows)
    }
    async getOneRus(req, res) {
        const id = req.params.id
        const item = await db.query(`SELECT * FROM rus WHERE id = $1`, [id])
        res.json(item.rows[0])
    }
    async updateRus(req, res) {
        const {id, task_id, task_type, task, task_img, answer, answer_img} = req.body
        const rus = await db.query(`UPDATE rus set task_id = $1, task_type = $2, task = $3, task_img = $4, answer = $5, answer_img = $6 WHERE id = $7 RETURNING *`, [task_id, task_type, task, task_img, answer, answer_img, id])
        res.json(rus.rows[0])
    }
    async deleteRus(req, res) {
        const id = req.params.id
        const rus = await db.query(`DELETE FROM rus WHERE id = $1`, [id])
        res.json(rus.rows[0])
    }
    async findRus(req, res) {
        const id = req.params.id
        const task = await db.query(`SELECT * FROM rus WHERE task_type = $1`, [id])
        res.json(task.rows)
    }
}

module.exports = new RusController()