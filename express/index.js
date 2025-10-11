import express from "express"
import fetch from "node-fetch"
import path from "path"
import {fileURLToPath} from "url"
import axios from "axios"
import session from "express-session"
import bodyParser from "body-parser"

const app = express();
const port = 3000;
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DJANGO_URL = "http://127.0.0.1:8000"

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
  if (req.session.user) {
    res.redirect('/product')
  }
  res.render('login')
})

app.get('/login', async (req, res) => {
  const {username, password} = req.body;

  try {
    const tokenRes = await axios.post(`${DJANGO_URL}/user/token/`, {username, password})
    const token = tokenRes.data.access

    res.redirect('/product')
    
  }
  catch (err) {
    res.send("Bad request")
  }

})

app.get('/product', async (req, res) => {
  if(!req.session.user){
    res.redirect('/login')
  }
  try {
    const product_list = fetch(`${DJANGO_URL}/product/`)
    const catogory_list = fetch(`${DJANGO_URL}/category/`)

  }
  catch (err) {
    res.status(500).json(`Error! : ${err}`);
    
  }
})

app.get('/logout', (req, res) => {
  req.session.destroy(() => res.redirect('/login'))
})

app.listen(port, () => {
  console.log(`listening port ${port}`);
})
