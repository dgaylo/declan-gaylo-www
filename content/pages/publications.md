Title: Publications
slug: publications
modified: 2025-03-24 00:00
ChangeFreq: monthly
Priority: 0.7

{% from 'templates/publications.html.jinja2' import journal_article, conference_presentation, thesis %}

## Journal Papers

{{ journal_article(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2024",
    title = "Effect of degassing on bubble populations in air-entraining free-surface turbulent flows",
    journal = "Journal of Fluid Mechanics",
    volume = "995",
    pages = "A12",
    doi = "10.1017/jfm.2024.780"
) }}

{{ journal_article(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2023",
    title = "Fundamental time scales of bubble fragmentation in homogeneous isotropic turbulence",
    journal = "Journal of Fluid Mechanics",
    volume = "962",
    pages = "A25",
    doi = "10.1017/jfm.2023.281"
) }}

{{ journal_article(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2022",
    title = "An Eulerian label advection method for conservative volume-based tracking of bubbles/droplets",
    journal = "Journal of Computational Physics",
    volume = "470",
    pages = "111560",
    doi = "10.1016/j.jcp.2022.111560"
) }}

{{ journal_article(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2021",
    title = "Effects of power-law entrainment on bubble fragmentation cascades",
    journal = "Journal of Fluid Mechanics",
    volume = "917",
    pages = "R1",
    doi = "10.1017/jfm.2021.333"
) }}

## Conference Presentations

{{ conference_presentation(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2024",
    month = "November",
    title = "Degassing-dominated bubble populations in air-entraining free-surface turbulence",
    conference = "77th Annual Meeting of the APS Division of Fluid Dynamics",
    city = "Salt Lake City",
    state = "UT"
)}}

{{ conference_presentation(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2024",
    month = "July",
    title = "Quantifying Entrainment and Degassing of Bubbles by Free-Surface Turbulence for Ship Wake Applications",
    conference = "35th Symposium on Naval Hydrodynamics",
    city = "Nantes",
    state = "France",
    pdf = "/files/Quantifying%20Entrainment%20and%20Degassing%20of%20Bubbles%20by%20Free-Surface%20Turbulence%20for%20Ship%20Wake%20Applications.pdf"
)}}

{{ conference_presentation(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2023",
    month = "November",
    title = "Quantifying bubble degassing in entraining free-surface turbulence",
    conference = "76th Annual Meeting of the APS Division of Fluid Dynamics",
    city = "Washington",
    state = "D.C."
)}}

{{ conference_presentation(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2022",
    month = "July",
    title = "Quantifying Fragmentation Statistics in Two-Phase Turbulent Flows for Ship Wake Applications",
    conference = "34th Symposium on Naval Hydrodynamics",
    city = "Washington",
    state = "D.C.",
    pdf = "/files/Quantifying%20Fragmentation%20Statistics%20in%20Two-Phase%20Turbulent%20Flows%20for%20Ship%20Wake%20Applications.pdf"
)}}

{{ conference_presentation(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2021",
    month = "November",
    title = "Effects of split power-law entrainment on bubble fragmentation cascades",
    conference = "74th Annual Meeting of the APS Division of Fluid Dynamics",
    city = "Phoenix",
    state = "AZ"
)}}

{{ conference_presentation(
    authors = "Gaylo, D. B., Hendrickson, K., & Yue, D. K.P.",
    year = "2020",
    month = "November",
    title = "Eulerian Label Advection method for bubble tracking in two-fluid Navier-Stokes simulations",
    conference = "73rd Annual Meeting of the APS Division of Fluid Dynamics",
    city = "Chicago",
    state = "IL"
)}}

## Academic Theses

{{ thesis(
    authors = "Gaylo, D. B.",
    year = "2021",
    title = "Effects of power-law entrainment on bubble fragmentation cascades",
    type = "Master's thesis",
    school = "Massachusetts Institute of Technology",
    city = "Cambridge",
    state = "MA",
    link = "https://hdl.handle.net/1721.1/139438"
)}}

{{ thesis(
    authors = "Gaylo, D. B., & Roske, D.",
    year = "2019",
    title = "[Pressure Effects of Transom Lift Devices on Prismatic Planing Hulls]({filename}/posts/undergradthesis.md)",
    type = "Bachelor's thesis",
    school = "Webb Institute",
    city = "Glen Cove",
    state = "NY",
    pdf = "/files/Pressure%20Effects%20of%20Transom%20Lift%20Devices%20on%20Prismatic%20Planing%20Hulls.pdf"
)}}
