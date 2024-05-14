import "./block.scss";
import InsertLinkOutlinedIcon from '@mui/icons-material/InsertLinkOutlined';


export default function Block(props) {
  const link = `http://127.0.0.1:8000/${props.shortLink}`
  return (
    <div className="block">
      <p className="link">
        <InsertLinkOutlinedIcon /><a href={link} target="_blank">{link}</a>
      </p>
      <div className="exportButtons"></div>
    </div>
  );
}
