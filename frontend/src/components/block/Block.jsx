import "./block.scss";

export default function Block(props) {
  return (
    <div className="block">
      <a className="link">{props.shortLink}</a>
      <div className="exportButtons"></div>
    </div>
  );
}
