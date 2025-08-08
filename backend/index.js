const express = require('express')
const cors = require('cors')
const mathsRouter = require('./routes/maths.routes')
const rusRouter = require('./routes/rus.routes')
const infRouter = require('./routes/inf.routes')
const usersRouter = require('./routes/users.routes')
const PORT = 59254

const app = express()
app.use(cors({
    origin: '*',
    credentials: true
}))

app.use(express.json())
app.use('/api', mathsRouter)
app.use('/api', rusRouter)
app.use('/api', infRouter)
app.use('/api', usersRouter)

app.listen(PORT, () => console.log(`server started on port ${PORT}`))
