import React from 'react';
import {NavLink} from 'react-router-dom';
import styled from 'styled-components';

const AddRecipeButton = () => {
  return (
    <BLink to={'/AddForm'}>Add Recipe</BLink>
  );
}

const BLink = styled(NavLink)`
  position: absolute;
  top: 20px;
  right: 20px; 
  text-decoration: none;
  padding: 10px 20px;
  background: linear-gradient(35deg, #494949, #313131); 
  color: white;
  border: none;
  border-radius: 2rem;
  cursor: pointer;
  font-size: 1.5rem;

  h4{
    color: white;
    font-size: 2rem;
}
svg{
    color: white;
    font-size: 1.5rem;
}
  &.active{
    background: linear-gradient(to right, #f27121, #e94057);
    svg{
        color: white;
    }
    h4{
        color: white;
    }
  `;

export default AddRecipeButton;
