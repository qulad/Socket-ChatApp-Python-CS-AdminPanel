import './App.css';
import { Navbar } from './components/Navbar';
import { Control } from './components/Control';
import { Commands } from './components/Commands';
import { ChangeIP } from './components/changeIP';
import { ChangePort } from './components/changePort';
import { ChangeFormat } from './components/changeFormat';
import { Rooms } from './components/Rooms';

function App() {
	return (
		<div className="App">
			<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
  integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
  crossorigin="anonymous"
/>
			{Navbar()}
			{Control()}
			{Commands()}
			{ChangeIP()}
			{ChangePort()}
			{ChangeFormat()}
			{/* {Rooms()} */}
		</div>
	);
}

export default App;
