const Router = require('express')
const router = new Router()
const rusController = require('../controller/rus.controller')

router.post('/rus', rusController.createRus)
router.get('/rus', rusController.getRus)
router.get('/rus/:id', rusController.getOneRus)
router.put('/rus', rusController.updateRus)
router.delete('/rus/:id', rusController.deleteRus)
router.get('/rus/find/:id', rusController.findRus)


module.exports = router