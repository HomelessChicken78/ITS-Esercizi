import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserAlbum from './json_album/UserAlbum'
import 'bootstrap/dist/css/bootstrap.css'
import UserCrud from './UserCrud'

function App() {
  return (
    <>
      {/* <UserAlbum></UserAlbum> */}
      <UserCrud />
    </>
  )
}

export default App
