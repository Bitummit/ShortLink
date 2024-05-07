import "./form.scss";
import { useState } from "react";
import axios from "axios";
import Block from "../block/Block";

export default function Form() {
  const [link, setLink] = useState("");
  const [shortLink, setShortLink] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    axios
      .post("http://127.0.0.1:8000/api/links/", {
        full_link: link,
      })
      .then((response) => {
        setShortLink(response.data.short_link);
      });
  }

  function handleChange(event) {
    setLink(event.target.value);
  }

  return (
    <div>
      <form className="form" onSubmit={handleSubmit}>
        <input type="text" className="inputField" onChange={handleChange} />
        <button type="Submit" disabled={!link}>
          Short!
        </button>
      </form>
      <Block shortLink={shortLink} />
    </div>
  );
}
