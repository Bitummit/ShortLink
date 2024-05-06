import "./form.scss";
import { useState } from "react";

export default function Form() {
  const [link, setLink] = useState("");

  function handleSubmit(event) {
    console.log(event.target);
    event.preventDefault();
  }

  function handleChange(event) {
    setLink(event.target.value)
  }

  return (
    <form className="form" onSubmit={handleSubmit}>
      <input type="text" className="inputField" onChange={handleChange}/>
      <button type="Submit" disabled={!link}>
        Short!
      </button>
    </form>
  );
}
