import React, { useEffect, useState } from "react";
import styled from 'styled-components';
import {useParams} from 'react-router-dom';

function Recipe() {
  let params = useParams();
  const [instructions, setInstructions] = useState([]);
  const [ingredients, setIngredients] = useState([]);
  const[activeTab, setActiveTab] = useState("instructions:");

  const fetchInstructions = async (name) => {
    const data = await fetch(`http://127.0.0.1:5000/api/info`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: name }),
  });
    const InstrucionData = await data.json();
    setInstructions(InstrucionData);
  }

  useEffect(() => {
    fetchInstructions(params.name);
  },[params.name]);

return (
  <div>
    {instructions.map((instructions, Recipe_ID) => (
    <DetailWrapper key={Recipe_ID}>
        <div >
          <h2>{instructions.recipe_name}</h2>
          <img src={instructions.imageUrl} height="350px" width="350px" alt="" />
        </div>
        <Info>
          <Button className={activeTab === 'instructions' ? 'active' :''} onClick={()=> setActiveTab("instructions")}>Instructions</Button>
          <Button className={activeTab === 'ingredients' ? 'active' :''} onClick={() => setActiveTab("ingredients")}>Ingredients</Button>
          {activeTab === 'instructions' &&(
            <div>
            <h2>Summary:</h2>
            <h3>Diet Type:</h3>
            <p>{instructions.dietary_needs}</p>
            <h3>Cuisine:</h3>
            <p>{instructions.cuisine}</p>
            <h3>Meal Type:</h3>
            <p>{instructions.meal_type}</p>
            <h3>Preparation Time:</h3>
            <p>{instructions.preparation_time} Minutes</p>
            <h3>Calorie:</h3>
            <p>{instructions.calorie} kcal</p>
            <h3>Carbohydrates:</h3>
            <p>{instructions.carbohydrates} Grams</p>
            <h3>Protein:</h3>
            <p>{instructions.protein} Grams</p>
            <h3>Fat:</h3>
            <p>{instructions.fat} Grams</p>
            <h3>Instructions:</h3>
            <p>{instructions.instructions}</p>
          </div>
          )}
        
        {activeTab === 'ingredients' && (
          <ul>
          <h3>Ingredients:</h3>
          <p>{instructions.ingredients}</p>
        </ul>
        )}
      </Info>
    </DetailWrapper>
    ))}
    </div>
  )
}

const DetailWrapper = styled.div`
  margin-top: 10rem;
  margin-bottom: 5rem;
  display: flex;
  .active{
    background: linear-gradient(35deg, #494949, #313131);
    color: white;
  }
  h2{
    margin-bottom: 2rem;
  }
  h3{
    font-size: 1rem;
    font-weight: 1rem;
  }
  li{
    font-size: 1rem;
    font-weight: 1rem;
    line-height: 2rem;
  }
  ul{
    margin-top: 2rem;
  }

`;

const Button = styled.button`
  padding: 1rem 2rem;
  color: #313131;
  background: white;
  border: 2px solid black;
  margin-right: 2rem;
  font-weight: 600;

`;

const Info = styled.div`
  margin-left: 10rem;
`;

export default Recipe