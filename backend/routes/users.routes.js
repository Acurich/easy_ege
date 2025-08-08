const Router = require('express')
const router = new Router()
const usersController = require('../controller/users.controller')

router.post('/users', usersController.createUser)
router.get('/users', usersController.getUsers)
router.get('/users/:id', usersController.getOneUser)
router.put('/users', usersController.updateUser)
router.delete('/users/:id', usersController.deleteUser)
router.get('/users/find/:id', usersController.findUser)


module.exports = router