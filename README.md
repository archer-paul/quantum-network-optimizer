# Quantum Optimization of Telefónica Deutschland's Telecom Network

## Overview
This project was conducted during my internship at Sopra Steria, in collaboration with my colleague Thibaud Chasteauneuf. The goal was to model Telefónica Deutschland's telecom network using cold atoms placed within the quantum computer of the French startup Pasqal. The primary objective was to optimize the network, as approximately 80% of outages or service interruptions for an operator are caused by network saturation.

## Methodology
1. **Network Modeling**:
   - We represented the telecom network as a set of qubits mapped to cold atoms.
   - The placement strategy aimed to reflect the real-world network topology.
2. **Optimization**:
   - Using quantum computing techniques, we sought to optimize the allocation of resources to reduce network saturation.
   - This involved finding the optimal configuration to handle high traffic loads efficiently.
3. **Simulation & Testing**:
   - The proposed placements were tested on an emulator of Pasqal's quantum machine.
   - Further testing on the actual quantum computer remains to be completed.

## Key Files
- `optimal_register_T&P.ipynb`: Contains the implementation of the telecom network model.
- `fast_optimal_register_T&P.ipynb`: An optimized version of the code, improving performance and efficiency.
- `optimal_register_with_strong_constraints_T&P.ipynb`: A version with stricter physical constraints, using the SLSQP method to enforce atom size and distribution limits on the grid.

## Future Work
- Testing the optimized model on Pasqal’s real quantum computer.
- Exploring further optimizations to enhance network performance.

## Acknowledgments
Special thanks to Sopra Steria and Pasqal for providing the opportunity to work on this cutting-edge quantum computing project.
A huge thank you to my colleague Thibaud Chasteauneuf for his valuable contributions to this work.
I would also like to warmly thank my internship supervisor, Charles Praud, for his guidance, availability, and passion throughout the project.
Finally, many thanks to Benjamin Yu for his insightful support and key help during the development process.