import Pages from "./pages/Pages";
import Category from "./components/Category";
import AddRecipeButton from "./components/AddRecipeButton"
import {BrowserRouter, Link} from 'react-router-dom';
import Search from "./components/Search";
import styled from 'styled-components';
import { SiCodechef } from "react-icons/si";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Nav>
          <SiCodechef />
          <Logo to={'/'}>EasyRecipes</Logo> 
        </Nav>
        <Search />
        <AddRecipeButton />
        <Category />
        <Pages />
      </BrowserRouter>
      
    </div>
  );
}

const Logo = styled(Link)`
  text-decoration: none;
  font-size: 2rem;
  font-weight: 400;
  font-family: 'Lobster Two', cursive;
`

const Nav = styled.div`
  padding: 4rem 0rem;
  display: flex;
  justify-content: center;
  align-items: center;
  svg{
    font-size: 2rem;
  }
`
export default App;
