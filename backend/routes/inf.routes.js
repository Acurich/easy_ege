const Router = require('express')
const router = new Router()
const infController = require('../controller/inf.controller')

router.post('/inf', infController.createInf)
router.get('/inf', infController.getInf)
router.get('/inf/:id', infController.getOneInf)
router.put('/inf', infController.updateInf)
router.delete('/inf/:id', infController.deleteInf)
router.get('/inf/find/:id', infController.findInf)


module.exports = router