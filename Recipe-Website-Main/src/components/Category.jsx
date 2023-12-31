import {FaPizzaSlice, FaHamburger} from 'react-icons/fa';
import {GiNoodles, GiChopsticks} from 'react-icons/gi';
import styled from "styled-components";
import {NavLink} from 'react-router-dom';

function Category() {
  return (
    <List>
        <SLink to={'/cuisine/Asian'}>
            <FaPizzaSlice />
            <h4>Asian</h4>
        </SLink>
        <SLink to={'/cuisine/American'}>
            <FaHamburger />
            <h4>American</h4>
        </SLink>
        <SLink to={'/cuisine/European'}>
            <GiNoodles />
            <h4>European</h4>
        </SLink>
    </List>
    
  );
}

const List = styled.div`
    display: flex;
    justify-content: center;
    margin: 2 rem 0rem;
`;

const SLink = styled(NavLink)`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    margin-right: 2rem;
    text-decoration: none;
    background: linear-gradient(35deg, #494949, #313131);
    width: 6rem:
    height: 6rem;
    cursor: pointer;
    transform: scale(0.5);
    padding: 1.5rem;

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
    }
`;

export default Category