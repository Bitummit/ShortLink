import { useState } from "react";
import "./App.scss";
import Form from "./components/form/Form";
import HandshakeOutlinedIcon from "@mui/icons-material/HandshakeOutlined";
import Block from "./components/block/Block";

function App() {
  const [shortLink, setShortLink] = useState("");

  return (
    <div className="app">
      <div className="content">
        <h1 className="title">
          <HandshakeOutlinedIcon className="icon" />
          Shorter
        </h1>
        <p>
          Помогите клиентам быстро найти вашу страницу в интернете. Благодаря
          короткой ссылке клиентам не придётся видеть длинные url-адреса,
          занимающие много места.
        </p>
        <Form setShortLink={setShortLink}/>
        <Block shortLink={shortLink}/>
      </div>
    </div>
  );
}

export default App;
