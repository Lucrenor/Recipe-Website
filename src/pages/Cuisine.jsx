import React, {useEffect, useState} from 'react'
import styled from 'styled-components';
import {motion} from 'framer-motion';
import {Link, useParams} from 'react-router-dom';

function Cuisine() {

  const [cuisine, setCuisine] = useState([]);
  let params = useParams();
  

  const getCuisine = async (name) => {
    const data = await fetch(`http://127.0.0.1:5000/api/get_cuisine`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: name }),
    });

    const recipes = await data.json();
    setCuisine(recipes);
};

  useEffect(() => {
    getCuisine(params.type);
  },[params.type]);


  return(
    <Grid>
        {cuisine.map((item) =>{
          console.log(item.imageUrl)
          return(
          
          <Grid>
            <Card key={item.Recipe_ID}>
              <Link to={'/recipe/'+item.Recipe_ID}>
              <img src={item.imageUrl} alt="" />
              <h4>{item.recipe_name}</h4>
              </Link>
            </Card>
          </Grid>
          )
        })}
    </Grid>
    )
}

const Grid = styled.div`
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr));
    grid-grap: 3rem;
`;
const Card = styled.div`
  img{
    width: 100%;
    border-radius: 2rem;
    padding: 1rem;
  }
  a{
    text_decoration: none;
  }
  h4{
    text-align: center;
    padding: 1rem;
  }
`;

export default Cuisine