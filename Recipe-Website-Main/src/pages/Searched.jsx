import React, {useEffect, useState} from 'react';
import {useParams, Link} from 'react-router-dom';
import styled from 'styled-components';

function Searched() {

    const [searchedRecipes, setSearchedRecipes] = useState([]);

    let params = useParams();

    useEffect(() => {
        getSearched(params.search);
    },[params.search]);


    const getSearched = async (name) => {
      const data = await fetch(`http://127.0.0.1:5000/api/search`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ name: name }),
      });
  
      const recipes = await data.json();
      setSearchedRecipes(recipes);
  };

  return(
    <Grid>
        {searchedRecipes.map((item) => {
            return(
                <Card key={item.Recipe_ID}>
                  
                  <Link to={'/recipe/'+item.Recipe_ID}>
                    <img src={item.imageurl} alt="" /> 
                    <h4>{item.Recipe_name}</h4>
                  </Link>
                </Card>
            )
        })}
    </Grid>
  )
}

const Grid = styled.div`
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
    grid-gap: 3rem;
`;
const Card = styled.div`
  img{
    width: 100%;
    border-radius: 2rem;
    padding: 1rem;
  }
  a{
    color: inherit;
    text_decoration: none;
  }
  h4{
    text-align: center;
    padding: 1rem;
  }
`;

export default Searched