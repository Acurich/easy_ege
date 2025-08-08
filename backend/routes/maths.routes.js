const Router = require('express')
const router = new Router()
const mathsController = require('../controller/maths.controller')

router.post('/maths', mathsController.createMaths)
router.get('/maths', mathsController.getMaths)
router.get('/maths/:id', mathsController.getOneMaths)
router.put('/maths', mathsController.updateMaths)
router.delete('/maths/:id', mathsController.deleteMaths)
router.get('/maths/find/:id', mathsController.findMaths)


module.exports = router