# SGH Practical Language Processing Project (Nov 2022)
An NUS-ISS text analytics project for the Singapore General Hospital (SGH) Corporate Communications team focusing on media monitoring.<br>
The project team comprised of:
1. Debbie Soon Ka Hui
2. Chua Tse Lert
3. Muhammad Firdaus Bin Osman
4. Boo Kai Xiang
5. Ervin Liu Wenyao

##  Project Components
*   Business understanding
*   Datasets (Data)
*   Data pre-processing, EDA and Model Development (Codebooks)

### Business Understanding
The goal of the project was to enable SGH corp comms to efficiently monitor its visibility on mainstream news media and public perception of its services and core values in action. In addition, the corp comms team frequently receives similar queries on publicity, design and event guidelines and requires a more efficient way to link users to answers available on the intranet but with which users may not be familiar or willing to navigate. <br>

To address the above needs, the team proposed and developed the following solutions:
*   Text summarization – to reduce the time the team needs for gisting media articles of interest
    - Finetuned T5 - refer to "T5 SGH" video under *Deployment Videos*
    - Finetuned BART - refer to "BART-Large Multi-News" and "BART-Large_SGH" videos under *Deployment Videos*
    - Finetuned Longformer Encoder-Decoder (LED) - refer to "LED SGH" and "LED Multi-News" videos under *Deployment Videos*

*   Text classification – to help the identify media articles showing SGH strategic pillars in action
    - Zero-shot classification (BART-large-mnli) - refer to "Zero-Shot" video under *Deployment Videos*
  
*   FAQ Chatbot – to aid the SGH team in responding to FAQs from internal staff on SGH public communications and design guidelines. A chatbot will relieve the manpower burden on the team to address these standard FAQ queries and help users to independently find the answers they need quickly.
    - Google DialogFlow - refer to "Ask Jerry Chatbot" video under *Deployment Videos*
