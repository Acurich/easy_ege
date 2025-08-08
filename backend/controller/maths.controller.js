const db = require('../db')
class MathsController {
    async createMaths(req, res) {
        try {
        const {task_id, task_type, task, task_img, answer, answer_img} = req.body
        const newMath = await db.query(`INSERT INTO maths (task_id, task_type, task, task_img, answer, answer_img) values ($1, $2, $3, $4, $5, $6) RETURNING *`, [task_id, task_type, task, task_img, answer, answer_img])
        res.json(newMath.rows[0])
        }
        catch (e) {
            res.status(500).json({"message": e})
        }
    }
    async getMaths(req, res) {
        const maths = await db.query(`SELECT * FROM maths`)
        res.json(maths.rows)
    }
    async getOneMaths(req, res) {
        const id = req.params.id
        const item = await db.query(`SELECT * FROM maths WHERE id = $1`, [id])
        res.json(item.rows[0])
    }
    async updateMaths(req, res) {
        const {id, task_id, task_type, task, task_img, answer, answer_img} = req.body
        const maths = await db.query(`UPDATE maths set task_id = $1, task_type = $2, task = $3, task_img = $4, answer = $5, answer_img = $6 WHERE id = $7 RETURNING *`, [task_id, task_type, task, task_img, answer, answer_img, id])
        res.json(maths.rows[0])
    }
    async deleteMaths(req, res) {
        const id = req.params.id
        const maths = await db.query(`DELETE FROM maths WHERE id = $1`, [id])
        res.json(maths.rows[0])
    }
    async findMaths(req, res) {
        const id = req.params.id
        const task = await db.query(`SELECT * FROM maths WHERE task_type = $1`, [id])
        res.json(task.rows)
    }
}

module.exports = new MathsController()