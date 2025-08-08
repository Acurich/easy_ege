const db = require('../db')
class InfController {
    async createInf(req, res) {
        try {
        const {task_id, task_type, task, task_img, answer, answer_img} = req.body
        const newInf = await db.query(`INSERT INTO inf (task_id, task_type, task, task_img, answer, answer_img) values ($1, $2, $3, $4, $5, $6) RETURNING *`, [task_id, task_type, task, task_img, answer, answer_img])
        res.json(newInf.rows[0])
        }
        catch (e) {
            res.status(500).json({"message": e})
        }
    }
    async getInf(req, res) {
        const inf = await db.query(`SELECT * FROM inf`)
        res.json(inf.rows)
    }
    async getOneInf(req, res) {
        const id = req.params.id
        const item = await db.query(`SELECT * FROM inf WHERE id = $1`, [id])
        res.json(item.rows[0])
    }
    async updateInf(req, res) {
        const {id, task_id, task_type, task, task_img, answer, answer_img} = req.body
        const inf = await db.query(`UPDATE inf set task_id = $1, task_type = $2, task = $3, task_img = $4, answer = $5, answer_img = $6 WHERE id = $7 RETURNING *`, [task_id, task_type, task, task_img, answer, answer_img, id])
        res.json(inf.rows[0])
    }
    async deleteInf(req, res) {
        const id = req.params.id
        const inf = await db.query(`DELETE FROM inf WHERE id = $1`, [id])
        res.json(inf.rows[0])
    }
    async findInf(req, res) {
        const id = req.params.id
        const task = await db.query(`SELECT * FROM inf WHERE task_type = $1`, [id])
        res.json(task.rows)
    }
}

module.exports = new InfController()