import express from "express"
import fetch from "node-fetch"
import path from "path"
import {fileURLToPath} from "url"

const app = express();
const port = 3000;
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/login', async (req, res) => {
})

app.get('/product', async (req, res) => {
  try {
    const product_list = fetch("http://127.0.0.1:8000/product/")
    const catogory_list = fetch("http://127.0.0.1:8000/category/")

  }
  catch (err) {
    res.status(500).json(`Error! : ${err}`);
    
  }
})

app.listen(port, () => {
  console.log(`listening port ${port}`);
})
