import React, {useEffect, useState} from 'react'
import styled from 'styled-components';
import {motion} from 'framer-motion';
import {Link, useParams} from 'react-router-dom';

function Cuisine() {

  const [cuisine, setCuisine] = useState([]);
  let params = useParams();
  

  const getCuisine =async (name) => {
      const data = await fetch(`https://api.spoonacular.com/recipes/complexSearch?apiKey=ff4c14fe16d14cbf8524945f5fe0b1c9&cuisine=${name}`);
      const recipes = await data.json();
      setCuisine(recipes.results);
  }

  useEffect(() => {
    getCuisine(params.type);
    console.log(params.type);
  },[params.type]);

  return(
    <Grid>
        {cuisine.map((item) =>{
          return(
          <Grid>
            <Card key={item.id}>
              <Link to={'/recipe/'+item.id}>
              <img src={item.image} alt="" />
              <h4>{item.title}</h4>
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