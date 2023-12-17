```markdown
# House-GAN: Automated Floor Plan Generation using Generative Adversarial Networks

## Overview

This repository contains the implementation of House-GAN, a novel approach for automated floor plan generation using machine learning techniques, specifically Generative Adversarial Networks (GANs). The system takes a bubble graph, a rough layout generated by an architect, as input and utilizes GANs to quickly iterate through multiple floor plan solutions based on user-specified constraints such as the number of rooms, room sizes, and spatial layout.

## Table of Contents

- [Introduction](#introduction)
- [Methodology](#methodology)
- [System Architecture](#system-architecture)
- [Machine Learning Model](#machine-learning-model)
- [Conv-MPN](#conv-mpn)
- [Training Dataset](#training-dataset)
- [Usage](#usage)
- [Results](#results)
- [Conclusion](#conclusion)
- [Acknowledgment](#acknowledgment)
- [References](#references)

## Introduction

The design of a home involves a complex balance between functionality and aesthetics, with floor plans playing a crucial role. House-GAN aims to automate the floor plan generation process using GANs, reducing time and costs associated with traditional methods. The system is designed to democratize home design, making architectural services more accessible to non-professionals through software automation.

## Methodology

House-GAN employs a combination of GANs and Conv-MPN (Convolutional Message Passing Networks) to process input bubble graphs and generate 2D floor plans. The system allows users to specify constraints through a web-based interface, enabling efficient iteration through multiple variations of a floor plan.

## System Architecture

The system operates as a web-based user interface, where users upload a bubble graph and input constraints for the proposed floor plan. GANs and Conv-MPN convert the input into a 2D floor plan, providing users with flexibility in selecting the final output. The system can also convert the final 2D output into a 3D floor plan using Pix2pix for enhanced visualization.

## Machine Learning Model

House-GAN uses Generative Adversarial Networks (GANs) to generate realistic floor plans. The model consists of a generator and a discriminator. The generator learns to create floor plans from bubble graphs, while the discriminator distinguishes between real and fake floor plans. The model is trained on a diverse dataset of over 10,000 floor plan images.

## Conv-MPN

Conv-MPN is a novel approach to Message Passing Neural Networks, utilizing convolution operations for efficient feature aggregation. This technique enhances the expressiveness of graph structures, making it suitable for tasks like floor plan generation.

## Training Dataset

The training dataset comprises over 10,000 diverse floor plan images in PNG format. It includes components such as openings, footprint, number of rooms, and bubble diagrams. The quality and diversity of this dataset are critical for the robustness and accuracy of the model.

## Usage

1. Clone the repository.
2. Install dependencies using `requirements.txt`.
3. Run the web-based user interface.
4. Upload a bubble graph and input constraints.
5. Explore and select generated floor plan variations.

## Results

The system outputs multiple 2D floor plan iterations based on user input and constraints. The results demonstrate the capability of House-GAN to generate high-quality floor plans comparable to those designed by human experts.

## Conclusion

House-GAN aims to revolutionize floor plan generation, addressing the limitations of current systems. It offers a user-friendly web interface, empowers users, and complements existing systems, contributing to increased automation in design.

## Acknowledgment

We acknowledge the support of Pillai College of Engineering (Autonomous), Navi Mumbai, and express gratitude to our project guide, Prof. Sheetal P Gawande, and the Department of Computer Engineering.

## References

- [Reference 1]
- [Reference 2]
- [Reference 3]
- [Reference 4]
- [Reference 5]
- [Reference 6]
- [Reference 7]
- [Reference 8]
- [Reference 9]
- [Reference 10]
- [Reference 11]

Feel free to explore the code and contribute to the project. For any inquiries, contact [Project Maintainer's Email].
```
