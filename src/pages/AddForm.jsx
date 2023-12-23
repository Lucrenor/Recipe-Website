import React, { useState } from 'react';
import styled from 'styled-components';

function AddForm() {
  const [formData, setFormData] = useState({
    Recipe_name: '',
    Dietary_needs: '',
    Cuisine: '',
    Meal_Type: '',
    Preparation_Time: '',
    Calorie: '',
    Carbohydrates: '',
    Protein: '',
    Fat: '',
    Instructions: '',
    Ingredients: '',
    ImgUrl: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        console.log('Recipe added successfully!');
        setFormData({
          Recipe_name: '',
          Dietary_needs: '',
          Cuisine: '',
          Meal_Type: '',
          Preparation_Time: '',
          Calorie: '',
          Carbohydrates: '',
          Protein: '',
          Fat: '',
          Instructions: '',
          Ingredients: '',
          ImgUrl: '',
        });
      } else {
        console.error('Failed to add recipe');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <FormContainer>
      <Title>Add Recipe Form</Title>
      <StyledForm onSubmit={handleSubmit}>
        <StyledLabel>
          Recipe Name:
          <InputField
            type="text"
            name="Recipe_name"
            value={formData.Recipe_name}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
          Dietary Needs:
          <InputField
            type="text"
            name="Dietary_needs"
            value={formData.Dietary_needs}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
          Cuisine:
          <InputField
            type="text"
            name="Cuisine"
            value={formData.Cuisine}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
          Meal Type:
          <InputField
            type="text"
            name="Meal_Type"
            value={formData.Meal_Type}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
          Preperation Time:
          <InputField
            type="text"
            name="Preparation_Time"
            value={formData.Preparation_Time}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
        Calorie:
          <InputField
            type="text"
            name="Calorie"
            value={formData.Calorie}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
        Carbohydrates:
          <InputField
            type="text"
            name="Carbohydrates"
            value={formData.Carbohydrates}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
        Protein:
          <InputField
            type="text"
            name="Protein"
            value={formData.Protein}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
        Fat:
          <InputField
            type="text"
            name="Fat"
            value={formData.Fat}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
        Instructions:
          <InputField
            type="text"
            name="Instructions"
            value={formData.Instructions}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
        Ingredients:
          <InputField
            type="text"
            name="Ingredients"
            value={formData.Ingredients}
            onChange={handleChange}
          />
        </StyledLabel>
        <StyledLabel>
        Image Url:
          <InputField
            type="text"
            name="ImgUrl"
            value={formData.ImgUrl}
            onChange={handleChange}
          />
        </StyledLabel>
        
        <SubmitButton type="submit">Submit</SubmitButton>
      </StyledForm>
    </FormContainer>
  );
}

export default AddForm;

const FormContainer = styled.div`
  text-align: center;
`;

const Title = styled.h2`
  font-size: 24px;
  margin-bottom: 20px;
`;

const StyledForm = styled.form`
  max-width: 600px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
`;

const StyledLabel = styled.label`
  margin-bottom: 15px;
  display: flex;
  flex-direction: column;
`;

const InputField = styled.input`
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  margin-top: 5px;
`;

const SubmitButton = styled.button`
  padding: 10px 20px;
  background-color: #313131;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-top: 20px;

  &:hover {
    background-color: #f27121;
  }
`;