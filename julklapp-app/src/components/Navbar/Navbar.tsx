import React from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import './Navbar.css';

function navbar() {

  return (
    <Navbar>
      <Container>
        <Nav.Link as={Link} to="/"><b>Home</b></Nav.Link>
        <Nav.Link as={Link} to="/about"><b>About</b></Nav.Link>
        <Nav.Link as={Link} to="/contact"><b>Contact</b></Nav.Link>
      </Container>
    </Navbar>
  );
}

export default navbar;